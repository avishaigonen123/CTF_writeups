const express = require('express');
const crypto = require('crypto');
const zlib = require('zlib');
const app = express();
const path = require('path');

app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

const PORT = 3000;
const key = crypto.randomBytes(32);
const notes = {};

app.get('/', (_req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

function generateNoteId() {
    return crypto.randomBytes(5).toString('hex').toUpperCase();
}

function notesToCSV() {
    const rows = [['title', 'note_id']];
    for (const id in notes) {
        const { title } = notes[id];
        // escape quotes by doubling them
        rows.push([title, id]);
    }
    return rows.map(r => r.join(',')).join("\n");
}

notes[generateNoteId()] = {
    title: "flag",
    content: "!BS{<REDACTED>}"
}

app.post('/note', (req, res) => {
    const { title, content } = req.body;
    if (!title || !content) {
        return res.status(400).json({ error: 'title and content required' });
    }

    const id = generateNoteId();
    notes[id] = { title, content };
    console.log("CREATED NOTE: ", notes[id])
    res.json({ id });
});

app.get('/note/:id', (req, res) => {
    const note = notes[req.params.id];
    if (!note?.title) {
        return res.status(404).json({ error: 'note not found' });
    }
    res.json(note);
});

app.put('/note/:id', (req, res) => {
    const note = notes[req.params.id];
    if (!note?.title) {
        return res.status(404).json({ error: 'note not found' });
    }

    const { title, content } = req.body;
    if (!title || !content) {
        return res.status(400).json({ error: 'title and content required' });
    }

    notes[req.params.id] = { title, content };
    res.json({ success: true });
});

app.get('/report', (req, res) => {
    const csv = notesToCSV()

    zlib.deflateRaw(csv, (err, deflated) => {
        if (err) {
            console.error(err);
            return res.status(500).json({ error: "Compression failed" });
        }

        const iv = crypto.randomBytes(12);
        const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);
        const encrypted = Buffer.concat([
            cipher.update(deflated),
            cipher.final()
        ]);

        res.json({
            encrypted: encrypted.toString('base64'),
        });
    });
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});