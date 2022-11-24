# Homework
import re
import os

# 1. Write a function that extracts the words from a given text as a parameter.
# A word is defined as a sequence of alpha-numeric characters.

def extract_words(text: str) -> list:
    return re.split(r"\W+", text)


# 2. Write a function that receives as a parameter a regex string, a text string and a whole number x,
# and returns those long-length x substrings that match the regular expression.

def match_length_x(regex: str, text: str, x: int) -> list:
    return [s for s in re.findall(f"{regex}", text) if len(s) == x]


# 3. Write a function that receives as a parameter a string of text characters and a list of regular expressions
# and returns a list of strings that match on at least one regular expression given as a parameter.

def match_any(regexes: list, text: str) -> list:
    result = []
    for regex in regexes:
        result.extend(re.findall(f"{regex}", text))
    return [set(result)]


# 4. Write a function that receives as a parameter the path to an xml document and an attrs dictionary
# and returns those elements that have as attributes all the keys in the dictionary and values the corresponding
# values. For example, if attrs={"class": "url", "name": "url-form", "data-id": "item"} the items selected will be
# those tags whose attributes are class="url" si name="url-form" si data-id="item".

def match_all_xml(path: str, attrs: dict) -> list | str:
    try:
        with open(path, "r") as f:
            tags = re.findall(r"<[^/>]+>", f.read())
            filtered = []
            for tag in tags:
                valid = True
                for key in attrs.keys():
                    if (re.search(f"{key}\s*=\s*\"{attrs[key]}\"", tag) == None):
                        valid = False
                        break
                if not valid:
                    continue
                filtered += [tag.split(" ")[0][1:]]
            return filtered
    except FileNotFoundError:
        return "Error on opening file."
    except Exception:
        return "Unknown error."


# 5. Write another variant of the function from the previous exercise that returns those elements
# that have at least one attribute that corresponds to a key-value pair in the dictionary.

def match_any_xml(path: str, attrs: dict) -> list | str:
    try:
        with open(path, "r") as f:
            tags = re.findall(r"<[^/>]+>", f.read())
            filtered = []
            for tag in tags:
                valid = True
                for key in attrs.keys():
                    if (re.search(f"{key}\s*=\s*\"{attrs[key]}\"", tag)):
                        filtered += [tag.split(" ")[0][1:]]
                        break
            return filtered
    except FileNotFoundError:
        return "Error on opening file."
    except Exception:
        return "Unknown error."


# 6. Write a function that, for a text given as a parameter, censures words that begin and end with vowels.
# Censorship means replacing characters from odd positions with *.

def censor_text(text: str) -> str :
    words = re.findall(r"[aeiouAEIOU]\w*[aeiouAEIOU]", text)
    censored_words = []
    for word in words:
        censored_word = ""
        for i in range(1, len(word) + 1):
            censored_word += word[i - 1] if i % 2 == 0 else "*"
        censored_words.append(censored_word)
    return re.sub(r"[aeiouAEIOU]\w*[aeiouAEIOU]", lambda x: censored_words.pop(0), text)


# 7. Verify using a regular expression whether a string is a valid CNP.

def validate_cnp(cnp: str) -> bool:
    # return re.match(r"[1-9][1-9]{2}((0[1-9])|(1[0-2]))((0[1-9])|([12]\d)|(3[01]))\d{6}", cnp) != None
    return re.match(r"^[1-9][0-9]{2}(0[1-9])|(1|2[0-9])|(30|1)\d{6}", cnp) != None and len(cnp) == 13

# 8. Write a function that recursively scrolls a directory and displays those files whose name matches
# a regular expression given as a parameter or contains a string that matches the same expression.
# Files that satisfy both conditions will be prefixed with ">>".

def match_files(dir: str, regex: str) -> list:
    matches = []
    if os.path.isdir(dir):
        paths = os.listdir(dir)
        subdirs = [p for p in paths if os.path.isdir(p)]
        files = [p for p in paths if os.path.isfile(p)]
        for s in subdirs:
            matches.extend([match_files(s, regex)])
        for f in files:
            file_name = os.path.splitext(f)[0]
            matches += [file_name]
            return matches


def main():
    text: str = "adwadjsk saf..aj?32g  asdaw!asdawd 23sdfd2"

    # print(extract_words(text))
    # print(match_length_x(r"\w+", text, 3))
    # print(match_any([r"\w+", r"\d", r"\W"], text))
    # print(match_all_xml("file.xml", {"class": "url", "name": "url-form", "data-id": "item"}))
    # print(match_any_xml("file.xml", {"class": "url", "name": "url-form", "data-id": "item"}))
    # print(censor_text("Ana are multe mere si nu stie ce sa faca cu ele"))
    # print(validate_cnp("5010829225891"))
    # print(match_files(r"C:\Users\alinh\Documents\Facultate\Semestrul V\Python\lab\Python\L6", r"\w"))

if __name__ == "__main__":
    main()