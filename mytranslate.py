#########################################################################################
EtoF = {"She": "Elle", "he": "il", "I": "Je", "me": "moi", "my": "mon",
        "mine": "mien", "her": "son", "his": "son", "him": "lui", "their": "leur", "them": "leur",
        "vacation": "vacances", "morning": "matin",
        "breakfast": "petit-déjeuner", "eat": "manger", "eating": "manger",
        "wake-up": "réveillez-vous", "in": "dans", "the": "le", "watch": "regarder", "movie": "film",
        "movies": "films", "read": "lis", "book": "livre", "books": "livres", "do": "faire", "no": "non",
        "not": "ne pas", "yes": "oui", "go": "aller", "went": "est allé", "out": "en dehors", "never": "jamais",
        "usually": "d'habitude", "call": "appel", "friends": "amis", "family": "famille", "time": "temps",
        "play": "jouer", "video-games": "jeux vidéos", "board-games": "jeux de société", "cook": "cuisiner",
        "for": "pour", "dinner": "dîner", "warm": "chaud", "winter": "hiver", "am": "suis", "busy": "occupé",
        "weekdays": "jours de la semaine", "did": "fait", "ate": "manger", "are": "sont", "was": "était",
        "were": "étaient", "have": "avoir", "has": "avoir", "good": "bien", "bad": "mal", "very": "très",
        "is": "est", "one": "un", "two": "deux", "and": "et", ".": ".", ",": ",", "!": "!"}
# This is the English to French word saved in a dictionary


def reverseDictionary(dictionary):
    # This function  reverses the English to French dictionary
    # So that,  I don't have to type in the entire dictionary manually
    FtoE = {}
    # This is an empty string
    for english, french in dictionary.items():
        FtoE[french] = english
    # Using a for loop, the french words has been replaced position and storing it in the empty string
    return FtoE
    # The French to English dictionary is returned

def EngtoFre(eng1):
    # This function converts English sentences to French sentences
    fre1 = ''
    # This is an empty string
    for i in eng1.split():
        if i in EtoF:
            fre1 += EtoF[i] + ' '
        else:
            fre1 += f'"{i}" '
    # Using a for loop and if function, it is checked if the entered word is in the dictionary
    # If the word is in the dictionary, the French word is added, if not, then the word is added with quotation
    return fre1
    # The French sentence is returned


def FretoEng(fre1):
    # This function converts French sentences to English sentences
    eng1 = ''
    # This is an empty string
    FtoE = reverseDictionary(EtoF)
    for i in fre1.split():
        if i in FtoE:
            eng1 += FtoE[i] + ' '
        else:
            eng1 += f'"{i}" '
    # Using a for loop and if function, it is checked if the entered word is in the dictionary
    # If the word is in the dictionary, the English word is added, if not, then the word is added with quotation
    return eng1
    # The English sentence is returned
#########################################################################################


EtoG = {"She": "Sie", "he": "er", "I": "Ich", "me": "mich", "my": "meine", "mine": "mir", "her": "ihr",
        "his": "seine", "him": "ihm", "vacation": "ferien", "morning": "morgen",
        "breakfast": "frühstück", "eat": "essen", "wake-up": "aufwachen", "in": "in", "watch": "sehen", "movie": "film",
        "movies": "filme", "read": "lesen", "book": "buch", "books": "bücher", "do": "machen", "no": "nein",
        "not": "nicht", "yes": "ja", "go": "gehen", "went": "ging", "out": "aus", "never": "nie",
        "usually": "gewöhnlich", "call" : "anruf", "friends": "freunde", "family": "familie", "time": "zeit",
        "play": "spielen", "video-games": "videospiele", "board-games": "brettspiele",
        "cook": "koch", "for": "zu", "dinner": "abendessen", "warm": "warm", "winter": "winter",
        "am": "bin", "busy": "beschäftigt", "the": "das", "weekdays": "wochentags", "did": "tun", "ate": "essen",
        "are": "sind", "was": "war", "were": "wurden", "have": "haben", "has": "hat",
        "good": "gut", "bad": "schlimm", "very": "sehr", "is": "ist","one": "einer", "two": "zwei", "and": "und",
        ".": ".", ",": ",", "!": "!"}
# This is the English to German word saved in a dictionary


def reverseDictionary1(dictionary):
    # This function  reverses the English to German dictionary
    # So that,  I don't have to type in the entire dictionary manually
    GtoE = {}
    # This is an empty string
    for english, german in dictionary.items():
        GtoE[german] = english
    # Using a for loop, the german words has been replaced position and storing it in the empty string
    return GtoE
    # The French to English dictionary is returned


def EngtoGer(eng1):
    # This function converts English sentences to German sentences
    ger1 = ''
    # This is an empty string
    for i in eng1.split():
        if i in EtoF:
            ger1 += EtoG[i] + ' '
        else:
            ger1 += f'"{i}" '
    # Using a for loop and if function, it is checked if the entered word is in the dictionary
    # If the word is in the dictionary, the German word is added, if not, then the word is added with quotation
    return ger1
    # The German sentence is returned


def GertoEng(ger1):
    # This function converts German sentences to English sentences
    eng1 = ''
    # This is an empty string
    GtoE = reverseDictionary(EtoG)
    for i in ger1.split():
        if i in GtoE:
            eng1 += GtoE[i] + ' '
        else:
            eng1 += f'"{i}" '
    # Using a for loop and if function, it is checked if the entered word is in the dictionary
    # If the word is in the dictionary, the English word is added, if not, then the word is added with quotation
    return eng1
    # The English sentence is returned
#########################################################################################


GtoF = {"Sie": "Elle", "er": "il", "Ich": "Je", "mich": "moi", "meine": "mon", "mir": "mien", "ihr": "son",
        "seine": "son", "ihm": "lui", "ferien": "vacances",
        "morgen": "martin", "frühstück": "petit-déjeuner", "aufwachen": "réveillez-vous", "in": "dans",
        "sehen": "regarder", "film": "film",
        "filme": "films", "lesen": "lis", "buch": "livre", "bücher": "livres", "machen": "faire",
        "nein": "non", "nicht": "ne pas", "ja": "oui", "gehen": "aller", "ging": "est allé",
        "aus": "en dehors", "nie": "jamais", "gewöhnlich": "dhabitude", "anruf": "appel",
        "freunde": "amis", "familie": "famille", "zeit": "temps",
        "spielen": "jouer", "videospiele": "jeux vidéos", "brettspiele": "jeux de société",
        "koch": "cuisiner", "zu": "pour", "abendessen": "dîner", "warm": "chaud", "winter": "hiver",
        "bin": "suis", "beschäftigt": "occupé", "das": "le", "wochentags": "jours de la semaine",
        "tun": "fait", "essen": "manger",
        "sind": "sont", "war": "était", "wurden": "étaient", "haben": "avoir", "hat": "avoir",
        "gut": "bien", "schlimm": "mal", "sehr": "très", "ist": "est","einer": "un", "zwei": "deux", "und": "et",
        ".": ".", ",": ",", "!": "!"}
# This is the German to French word saved in a dictionary


def reverseDictionary2(dictionary):
    # This function  reverses the German to French dictionary
    # So that,  I don't have to type in the entire dictionary manually
    FtoG = {}
    # This is an empty string
    for german, french in dictionary.items():
        FtoG[french] = german
    # Using a for loop, the german words has been replaced position and storing it in the empty string
    return FtoG
    # The French to German dictionary is returned


def GertoFre(ger1):
    # This function converts German sentences to French sentences
    fre1 = ''
    # This is an empty string
    for i in ger1.split():
        if i in GtoF:
            fre1 += GtoF[i] + ' '
        else:
            fre1 += f'"{i}" '
    # Using a for loop and if function, it is checked if the entered word is in the dictionary
    # If the word is in the dictionary, the French word is added, if not, then the word is added with quotation
    return fre1
    # The French sentence is returned


def FretoGer(fre1):
    # This function converts French sentences to German sentences
    ger1 = ''
    # This is an empty string
    FtoG = reverseDictionary(GtoF)
    for i in fre1.split():
        if i in FtoG:
            ger1 += FtoG[i] + ' '
        else:
            ger1 += f'"{i}" '
    # Using a for loop and if function, it is checked if the entered word is in the dictionary
    # If the word is in the dictionary, the German word is added, if not, then the word is added with quotation
    return ger1
    # The German sentence is returned
#########################################################################################
Input = input("Please enter your sentence: ")
# The input function asks to input tge desired sentence
print("German: ", EngtoGer(Input))
# This prints the English to German translation of the entered sentence
print("French: ", EngtoFre(Input))
# This prints the English to French translation of the entered sentence
# The user can change the function name as they wish to translate between the three languages English, French and German
