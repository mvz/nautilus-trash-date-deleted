import gio

import nautilus

class ColumnExtension(nautilus.ColumnProvider, nautilus.InfoProvider):
  def __init__(self):
    pass
  
  def get_columns(self):
    return nautilus.Column("NautilusPython::date_deleted_column",
			   "date_deleted",
			   "Date Deleted",
			   "Get the date deleted"),

  def update_file_info(self, file):
    uri = file.get_uri()

    giofile = gio.File(uri)

    if giofile.get_uri_scheme() != "trash" or not giofile.query_exists():
      return

    info = giofile.query_info("trash")

    date = info.get_attribute_as_string("trash::deletion-date")

    if date == None:
      date = ""

    file.add_string_attribute('date_deleted', date)
