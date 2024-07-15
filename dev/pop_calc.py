import os

os.system("touch /tmp/ahmsec_was_here")
os.system("open -a Calculator")
os.system("unset GTK_PATH; unset GIO_MODULE_DIR; gnome-calculator &")
