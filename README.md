
// Choose directory to store everything. We will now call this top_dir

1. Copy 1_setupFolders.py to top_dir and run
2. Copy 2_orgFiles to top_dir
3. Copy the download zip from the customer (containing the top output) to top_dir and extract. The extract should contain folder containing more zip files which you should extract
4. In 2_orgFiles.py confirm the ms_file_top variable (depends on what customer called their file) and the sub_dirs (easier to change the extracted sub dirs to match)
5. Navigate to top_dir/shard_output, connect to any local mogosh and run:
    load( "3_dailyopsfromtop.js")
