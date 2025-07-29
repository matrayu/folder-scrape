#!/usr/bin/env python3
"""
Folder Scanner - A tool to traverse directories and output detailed file information.
"""

import os
import sys
import argparse
from datetime import datetime
from pathlib import Path


def get_file_type(file_path):
    """Determine the type of file based on extension."""
    if os.path.isdir(file_path):
        return "Directory"
    
    extension = Path(file_path).suffix.lower()
    if not extension:
        return "No Extension"
    
    # Common file type mappings
    file_types = {
        '.txt': 'Text File',
        '.pdf': 'PDF Document',
        '.doc': 'Word Document',
        '.docx': 'Word Document',
        '.xls': 'Excel Spreadsheet',
        '.xlsx': 'Excel Spreadsheet',
        '.jpg': 'JPEG Image',
        '.jpeg': 'JPEG Image',
        '.png': 'PNG Image',
        '.gif': 'GIF Image',
        '.mp3': 'MP3 Audio',
        '.mp4': 'MP4 Video',
        '.zip': 'ZIP Archive',
        '.py': 'Python Script',
        '.js': 'JavaScript File',
        '.html': 'HTML File',
        '.css': 'CSS File',
        '.json': 'JSON File',
        '.xml': 'XML File',
        '.csv': 'CSV File',
        '.md': 'Markdown File',
    }
    
    return file_types.get(extension, f'{extension[1:].upper()} File')


def format_size(size_bytes):
    """Convert bytes to human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} PB"


def scan_directory(directory_path):
    """
    Traverse directory and collect file information.
    
    Args:
        directory_path: Path to the directory to scan
        
    Returns:
        List of dictionaries containing file information
    """
    results = []
    
    for root, dirs, files in os.walk(directory_path):
        # Process directories
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            try:
                stat_info = os.stat(dir_path)
                created_time = datetime.fromtimestamp(stat_info.st_ctime)
                
                results.append({
                    'name': dir_name,
                    'path': dir_path,
                    'type': 'Directory',
                    'size': '-',
                    'created': created_time.strftime('%Y-%m-%d %H:%M:%S')
                })
            except (OSError, IOError) as e:
                results.append({
                    'name': dir_name,
                    'path': dir_path,
                    'type': 'Directory',
                    'size': 'Error',
                    'created': 'Error: ' + str(e)
                })
        
        # Process files
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                stat_info = os.stat(file_path)
                file_size = stat_info.st_size
                created_time = datetime.fromtimestamp(stat_info.st_ctime)
                file_type = get_file_type(file_path)
                
                results.append({
                    'name': file_name,
                    'path': file_path,
                    'type': file_type,
                    'size': format_size(file_size),
                    'created': created_time.strftime('%Y-%m-%d %H:%M:%S')
                })
            except (OSError, IOError) as e:
                results.append({
                    'name': file_name,
                    'path': file_path,
                    'type': 'Unknown',
                    'size': 'Error',
                    'created': 'Error: ' + str(e)
                })
    
    return results


def output_results(results, output_file=None):
    """
    Output results in tab-separated format.
    
    Args:
        results: List of file information dictionaries
        output_file: Optional file path to write results to
    """
    headers = ['File Name', 'Full Path', 'File Type', 'Size', 'Date Created']
    
    # Prepare output lines
    lines = []
    lines.append('\t'.join(headers))
    
    for item in results:
        line = '\t'.join([
            item['name'],
            item['path'],
            item['type'],
            item['size'],
            item['created']
        ])
        lines.append(line)
    
    # Output to console or file
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        print(f"Results written to: {output_file}")
    else:
        print('\n'.join(lines))


def main():
    """Main function to handle command-line arguments and execute the scan."""
    parser = argparse.ArgumentParser(
        description='Scan a directory and output detailed file information in tab-separated format.'
    )
    parser.add_argument(
        'directory',
        help='Path to the directory to scan'
    )
    parser.add_argument(
        '-o', '--output',
        help='Output file path (if not specified, prints to console)',
        default=None
    )
    
    args = parser.parse_args()
    
    # Validate directory
    if not os.path.exists(args.directory):
        print(f"Error: Directory '{args.directory}' does not exist.")
        sys.exit(1)
    
    if not os.path.isdir(args.directory):
        print(f"Error: '{args.directory}' is not a directory.")
        sys.exit(1)
    
    # Perform scan
    print(f"Scanning directory: {args.directory}")
    results = scan_directory(args.directory)
    
    # Output results
    print(f"Found {len(results)} items.")
    output_results(results, args.output)


if __name__ == '__main__':
    main()