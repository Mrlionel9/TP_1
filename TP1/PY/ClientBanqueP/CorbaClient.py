import sys 
import os
from omniORB import CORBA, PortableServer 

# \\CHEMINS ET IMPORTS ---
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



import org.fimproso# Import generated Python stubs 

 
def main(argv): 
   try: 
       # ORB initialization arguments 
       orb_args = ["-ORBInitRef", "NameService=corbaname::localhost:1050"] 
       # Initialize the ORB with arguments 
       orb = CORBA.ORB_init(argv + orb_args, CORBA.ORB_ID) 
       # Obtain a reference to the root context of the NameService using the ORB 
       obj = orb.resolve_initial_references("NameService") 
       naming_service = obj._narrow(CosNaming.NamingContext) 
       if naming_service is None: 
           print("Failed to narrow the NameService reference") 
           sys.exit(1) 
       # Resolve the Object reference from the NameService 
       name = [CosNaming.NameComponent("OperationBancaire", "")] 
       objref = naming_service.resolve(name) 
       # Narrow the Object reference to the appropriate type (OperationBancaire) 
       operation_bancaire = objref._narrow(org.fimproso.OperationBancaire) 
 
       if operation_bancaire is None: 
           print("Object reference is not an OperationBancaire") 
           sys.exit(1) 
 
       # Call methods on the OperationBancaire interface 
       balance = operation_bancaire.balance() 
       print(f"initial Balance: {balance}") 
 
       amount_to_deposit = 150.0 
       operation_bancaire.depot(amount_to_deposit) 
       print(f"deposited {amount_to_deposit}") 
       balance = operation_bancaire.balance() 
       print(f"current Balance: {balance}") 
 
       amount_to_withdraw = 300.0 
       operation_bancaire.retrait(amount_to_withdraw) 
       print(f"withdrew {amount_to_withdraw}") 
       balance = operation_bancaire.balance() 
       print(f"final Balance: {balance}") 
 
   except CORBA.Exception as e: 
       print(f"Error: {e}") 
 
   # Clean up 
   orb.shutdown(False) 
   orb.destroy() 
 
if __name__ == "__main__": 
   main(sys.argv) 