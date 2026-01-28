import re

def verifier_password(password):
    # Critères de sécurité
    longueur_min = 12
    has_upper = re.search(r"[A-Z]", password)
    has_lower = re.search(r"[a-z]", password)
    has_digit = re.search(r"\d", password)
    has_special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    score = 0
    feedback = []

    # Vérification des critères
    if len(password) >= longueur_min:
        score += 1
    else:
        feedback.append("- Doit contenir au moins 12 caractères")

    if has_upper and has_lower:
        score += 1
    else:
        feedback.append("- Doit contenir des majuscules et minuscules")

    if has_digit:
        score += 1
    else:
        feedback.append("- Doit contenir au moins un chiffre")

    if has_special:
        score += 1
    else:
        feedback.append("- Doit contenir un caractère spécial")

    # Résultat
    if score == 4:
        return "Fort : Votre mot de passe est sécurisé."
    elif score >= 2:
        return "Moyen : Améliorez votre sécurité avec ces points :\n" + "\n".join(feedback)
    else:
        return "Faible : Mot de passe dangereux !\n" + "\n".join(feedback)

# Test du script
print("--- Analyseur de Sécurité ---")
test = input("Entrez un mot de passe à tester : ")
print(verifier_password(test))
