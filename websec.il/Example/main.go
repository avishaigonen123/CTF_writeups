package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
	"io"
	"path/filepath"
	"strings"
)

func fdHandler(w http.ResponseWriter, r *http.Request) {
	path := r.URL.Query().Get("filepath")
	if path == "" {
		http.Error(w, "Missing 'filepath' query parameter", http.StatusBadRequest)
		return
	}

	file, err := os.Open(path)
	if err != nil {
		http.Error(w, fmt.Sprintf("Error opening file: %v", err), http.StatusInternalServerError)
		return
	}
	defer file.Close()

	filename := filepath.Clean(file.Name())
	data, err := io.ReadAll(file)
	if err != nil {
		http.Error(w, fmt.Sprintf("Error reading file: %v", err), http.StatusInternalServerError)
		return
	}

	if strings.Contains(filename, "flag") {
		http.Error(w, "This file is NOT allowed!!", http.StatusBadRequest)
		return
	}

	fmt.Fprintf(w, "%s", data)
}

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Query().Get("filepath") != "" {
			fdHandler(w, r)
			return
		}
		http.ServeFile(w, r, "fast_cow.html")
	})

	fmt.Println("Server running on http://localhost:8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
