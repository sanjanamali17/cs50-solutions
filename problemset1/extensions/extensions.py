filename = input("File name: ")

normalized = filename.strip().lower()

if normalized.endswith(".gif"):
    print("image/gif")
elif normalized.endswith(".jpg") or normalized.endswith(".jpeg"):
    print("image/jpeg")
elif normalized.endswith(".png"):
    print("image/png")
elif normalized.endswith(".pdf"):
    print("application/pdf")
elif normalized.endswith(".txt"):
    print("text/plain")
elif normalized.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
