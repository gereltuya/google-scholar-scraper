for i in range(0, 0): # former range was (0, 49)
    
    start_page = i*20

    params = {
      "api_key": "", # removed key for security reasons
      "device": "desktop",
      "engine": "google_scholar",
      "q": "artificial intelligence climate change",
      "hl": "en",
      "scisbd": "0",
      "num": "20",
      "start": str(start_page)
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    
    results_filename = "data/results" + str(i) + ".json"
    
    with open(results_filename, "w") as results_file:
        json.dump(results, results_file)
    
    print("printed: " + results_filename)
