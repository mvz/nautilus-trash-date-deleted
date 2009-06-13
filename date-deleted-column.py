import gio
import os

import nautilus

class ColumnExtension(nautilus.ColumnProvider, nautilus.InfoProvider):
  def __init__(self):
    pass
  
  def get_columns(self):
    return (nautilus.Column("NautilusPython::date_deleted_column",
			   "date_deleted",
			   "Date Deleted",
			   "Get the date deleted"),
    nautilus.Column("NautilusPython::original_path_column",
			   "original_path",
			   "Original Location",
			   "Get the original location"),)

  def update_file_info(self, file):
    uri = file.get_uri()

    giofile = gio.File(uri)

    if giofile.get_uri_scheme() != "trash" or not giofile.query_exists():
      return

    info = giofile.query_info("trash")

    date = info.get_attribute_as_string("trash::deletion-date")

    if date == None:
      date = ""

    path = info.get_attribute_as_string("trash::orig-path")

    if path == None:
      path = ""

    path = os.path.dirname(path)

    file.add_string_attribute('date_deleted', date)
    file.add_string_attribute('original_path', path)
