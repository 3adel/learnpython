
text = """Angesichts der Spannungen auf der koreanischen Halbinsel haben Nord- und Südkorea sich auf weitere hochrangige Gespräche verständigt. In einer gemeinsamen Mitteilung erklärten die Nachbarländer nach ihrem ersten offiziellen Treffen seit mehr als zwei Jahren, sie wollten die "aktuellen militärischen Spannungen entschärfen" und dazu den wiederaufgenommenen Dialog fortführen.
"""


splittedText = text.split(' ')
splittedTextNoDots = []

for word in splittedText:
    splittedTextNoDots.append(word.replace('.',''))


print(splittedTextNoDots)
