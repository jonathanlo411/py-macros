
# Functional Alias
hold() {
    # Save Cur Dir
    cur_dir=${pwd}
    cd ~/py-macros
    py hold.py -k "$1"
    cd $cur_dir
}