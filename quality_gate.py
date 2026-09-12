accuracy = 0.90
threshold = 0.80

print(f"Accuracy: {accuracy}")
print(f"Required accuracy: {threshold}")

if accuracy >= threshold:
    print("QUALITY GATE PASSED")
else:
    print("QUALITY GATE FAILED")
    raise SystemExit(1)
