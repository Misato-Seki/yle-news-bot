from datetime import datetime, timedelta

def get_yesterday_date():
    """
    Returns yesterday's date.
    """
    return (datetime.now() - timedelta(days=1)).date()

def is_yesterday(date_str, date_format="%Y-%m-%d"):
    """
    Checks if the given date string is yesterday's date.
    
    Args:
        date_str (str): The date string to check.
        date_format (str): The format of the date string. Default is "%Y-%m-%d".
        
    Returns:
        bool: True if the date string is yesterday's date, False otherwise.
    """
    try:
        # current_year = datetime.now().year
        parse_date = datetime.strptime(date_str, date_format).date()
        return parse_date == get_yesterday_date()
    except ValueError:
        return False