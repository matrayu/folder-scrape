# Folder Scanner

A Python command-line tool that recursively scans directories and generates detailed reports of all files and folders in tab-separated format.

## Features

- = **Recursive directory traversal** - Scans all subdirectories and files
- =Ê **Tab-separated output** - Easy to import into Excel, Google Sheets, or databases
- =Á **Smart file type detection** - Identifies file types based on extensions
- =Ï **Human-readable file sizes** - Converts bytes to KB, MB, GB, etc.
- =Å **File metadata** - Captures creation dates and full paths
- =¾ **Flexible output** - Display on console or save to file

## Installation

No installation required! This is a standalone Python script that uses only standard library modules.

### Requirements

- Python 3.6 or higher
- No external dependencies

## Usage

### Basic Usage

Scan a directory and display results in the console:

```bash
python folder_scanner.py /path/to/directory
```

### Save to File

Scan a directory and save results to a tab-separated file:

```bash
python folder_scanner.py /path/to/directory -o output.tsv
```

### Examples

```bash
# Scan current directory
python folder_scanner.py .

# Scan home directory and save to file
python folder_scanner.py ~ -o home_scan.tsv

# Scan specific project folder
python folder_scanner.py /Users/username/Projects -o projects_inventory.tsv
```

## Output Format

The tool generates tab-separated output with the following columns:

| Column | Description | Example |
|--------|-------------|---------|
| File Name | Name of the file or directory | `document.pdf` |
| Full Path | Complete path to the item | `/Users/john/Documents/document.pdf` |
| File Type | Type based on extension | `PDF Document` |
| Size | Human-readable size | `2.45 MB` |
| Date Created | Creation timestamp | `2024-01-15 14:30:22` |

### Supported File Types

The scanner recognizes common file types including:
- Documents (PDF, Word, Excel)
- Images (JPEG, PNG, GIF)
- Audio/Video (MP3, MP4)
- Code files (Python, JavaScript, HTML, CSS)
- Data files (JSON, XML, CSV)
- Archives (ZIP)
- And many more...

## Error Handling

- Permission errors are caught and reported in the output
- Invalid paths are detected before scanning begins
- Symbolic links are followed safely

## Use Cases

- **Disk space analysis** - Identify large files and folders
- **File inventory** - Create a catalog of files for documentation
- **Data migration** - Plan and track file transfers
- **Compliance auditing** - Document file types and locations
- **Backup planning** - Identify what needs to be backed up

## Contributing

Feel free to submit issues or pull requests to improve this tool.

## License

This project is open source and available under the MIT License.