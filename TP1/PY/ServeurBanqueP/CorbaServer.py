import sys
import os
from omniORB import CORBA, PortableServer

# CHEMINS ET IMPORTS 
try:
    
    cos_path = os.path.join(sys.prefix, 'Lib', 'site-packages', 'COS')
    if cos_path not in sys.path:
        sys.path.append(cos_path)
    
    
    import CosNaming_idl
    CN = CosNaming_idl._GlobalIDL.CosNaming # Chemin universel omniORB
except Exception:
    try:
        import CosNaming
        CN = CosNaming
    except ImportError:
        print("[ERREUR] Impossible de trouver le module CosNaming.")
        sys.exit(1)



import org.fimproso        
import org__POA.fimproso   


class OperationBancaire_i(org__POA.fimproso.OperationBancaire):
    def __init__(self):
        self._balance = 1000.0

    def balance(self):
        print(f"Demande de solde reçue : {self._balance}")
        return self._balance

    def depot(self, montant):
        self._balance += montant
        print(f"Dépôt de {montant} effectué. Nouveau solde : {self._balance}")

    def retrait(self, montant):
        self._balance -= montant
        print(f"Retrait de {montant} effectué. Nouveau solde : {self._balance}")

def main():
    try:
        # Initialisation de l'ORB
        orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

        
        poa = orb.resolve_initial_references("RootPOA")
        poa_manager = poa._get_the_POAManager()
        poa_manager.activate()

        # Création de l'instance du serviteur
        servant = OperationBancaire_i()
        
        # Obtention de la référence CORBA de l'objet
        obj = servant._this()

        # Enregistrement dans le NameService (Annuaire)
        ns_obj = orb.resolve_initial_references("NameService")
        naming_context = ns_obj._narrow(CosNaming.NamingContext)
        
        # On lie l'objet au nom "OperationBancaire"
        name = [CosNaming.NameComponent("OperationBancaire", "")]
        naming_context.rebind(name, obj)

        print("------------------------------------------")
        print("SERVEUR BANQUE PYTHON : Prêt et en attente")
        print("Port: 1050 | Nom: OperationBancaire")
        print("------------------------------------------")

        # Lancement de l'ORB 
        orb.run()

    except Exception as e:
        print(f"Erreur fatale du serveur : {e}")

if __name__ == "__main__":
    main()