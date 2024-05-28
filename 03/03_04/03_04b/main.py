user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}

def update_preferences(user_pref):
  return {k: v for k, v in user_pref.items() if v is not None}
    # clean_dict = {}
    # for k, v in user_pref.items():
    #     if v is not None:
    #         clean_dict[k] = v
    # return clean_dict


print(update_preferences(user_preferences))
