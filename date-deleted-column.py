import gio

import nautilus

class ColumnExtension(nautilus.ColumnProvider, nautilus.InfoProvider):
  def __init__(self):
    pass
  
  def get_columns(self):
    return nautilus.Column("NautilusPython::date_deleted_column",
			   "date_deleted",
			   "Date deleted",
			   "Get the date deleted"),

  def update_file_info(self, file):
    loc = file.get_location()

    info = loc.query_info("trash")

    if info.list_attributes("trash") == []:
      return

    file.add_string_attribute('date_deleted', info.get_attribute_as_string("trash::deletion-date"))
