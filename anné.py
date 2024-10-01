# Fonction pour tester si une année est bissextile
def est_bissextile(annee):
    if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
        return True
    return False

# Fonction pour donner le nombre de jours dans un mois
def jours_dans_mois(mois, annee):
    if mois < 1 or mois > 12:
        return None  # Mois invalide
    # Nombre de jours par mois
    jours_par_mois = [31, 29 if est_bissextile(annee) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return jours_par_mois[mois - 1]

# Fonction pour vérifier si une date est valide
def est_date_valide(jour, mois, annee):
    # Vérifier la validité des paramètres mois et année
    if mois < 1 or mois > 12 or annee < 1:
        return False
    
    # Vérifier si le jour est valide pour le mois et l'année donnés
    jours_max = jours_dans_mois(mois, annee)
    if jours_max is None or jour < 1 or jour > jours_max:
        return False
    
    return True

# Fonction principale
def main():
    # Saisie de la date par l'utilisateur
    try:
        jour = int(input("Entrez le jour: "))
        mois = int(input("Entrez le mois: "))
        annee = int(input("Entrez l'année: "))
        
        # Validation de la date
        if est_date_valide(jour, mois, annee):
            print("Date valide.")
        else:
            print("Date non valide.")
    except ValueError:
        print("Entrée invalide. Veuillez saisir des nombres entiers pour le jour, le mois et l'année.")

# Exécution du programme principal
if __name__ == "__main__":
    main()
