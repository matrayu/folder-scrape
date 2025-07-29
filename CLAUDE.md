# CLAUDE.md - Project Context for AI Assistants

## Project Overview

**Folder Scanner** is a Python command-line utility that recursively traverses directories and generates detailed file inventories in tab-separated format. The tool is designed to be simple, dependency-free, and cross-platform.

## Project Structure

```
folder-scrape/
├── folder_scanner.py    # Main script with all functionality
├── README.md           # User documentation
├── CLAUDE.md          # This file - AI assistant context
└── .gitignore         # Git ignore patterns
```

## Key Technical Details

### Architecture
- **Single-file script** - All functionality contained in `folder_scanner.py`
- **No external dependencies** - Uses only Python standard library
- **Python 3.6+** - Minimum version requirement
- **Cross-platform** - Works on Windows, macOS, and Linux

### Core Components

1. **`get_file_type(file_path)`** - Determines file type based on extension
2. **`format_size(size_bytes)`** - Converts bytes to human-readable format
3. **`scan_directory(directory_path)`** - Main traversal logic using `os.walk()`
4. **`output_results(results, output_file)`** - Formats and outputs data
5. **`main()`** - CLI argument parsing and orchestration

### Data Structure

Each scanned item is stored as a dictionary:
```python
{
    'name': str,      # File/directory name
    'path': str,      # Full absolute path
    'type': str,      # File type description
    'size': str,      # Formatted size or '-' for directories
    'created': str    # Creation timestamp
}
```

## Development Guidelines

### When Adding Features

1. **Maintain simplicity** - Avoid adding dependencies unless absolutely necessary
2. **Error handling** - Wrap file operations in try/except blocks
3. **Cross-platform** - Test path handling on different OS
4. **Performance** - Consider memory usage for large directory trees

### Common Enhancement Requests

- **Additional metadata** - Modified date, permissions, owner
- **Filter options** - Include/exclude patterns, file types
- **Output formats** - CSV, JSON, XML
- **Progress indicator** - For large scans
- **Parallel processing** - For faster scanning

### Testing Commands

```bash
# Test basic functionality
python folder_scanner.py .

# Test output to file
python folder_scanner.py . -o test_output.tsv

# Test error handling (non-existent directory)
python folder_scanner.py /path/that/does/not/exist

# Test with system directories (may have permission issues)
python folder_scanner.py /etc -o system_scan.tsv
```

## Code Style

- **PEP 8 compliant** - Follow Python style guidelines
- **Docstrings** - Use for all functions
- **Type hints** - Consider adding for clarity
- **Comments** - Explain complex logic, not obvious code

## Performance Considerations

- Uses `os.walk()` for efficient traversal
- Single-pass scanning
- Memory usage scales with directory count, not file size
- No caching or state between runs

## Security Notes

- Follows symbolic links (could lead to loops)
- Requires read permissions on scanned directories
- Does not modify any files
- Output may contain sensitive file paths

## Future Improvements to Consider

1. **Add `--exclude` pattern matching**
2. **Implement `--max-depth` for limiting traversal**
3. **Add JSON output format option**
4. **Include file hash calculation option**
5. **Add summary statistics at the end**
6. **Implement progress bar for large scans**
7. **Add option to skip symbolic links**
8. **Support for multiple input directories**

## Debugging Tips

- Use `-o` to save output for analysis
- Check permissions with `ls -la` on Unix systems
- Use `print()` statements to trace execution flow
- Test with small directory trees first
- Verify output format with spreadsheet software

## Git Workflow

```bash
# Check status
git status

# Add files
git add .

# Commit changes
git commit -m "Description of changes"

# Push to remote (once configured)
git push origin main
```

Remember: This tool is meant to be simple and reliable. Resist the urge to over-engineer!