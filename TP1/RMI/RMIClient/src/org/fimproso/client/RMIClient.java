package org.fimproso.client;

import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import org.fimproso.rmi.OperationBancaire;

public class RMIClient {

    public static void main(String[] args) {
        try {
            String url = "rmi://localhost:5099/Bank";
            OperationBancaire operationBancaire =
                    (OperationBancaire) Naming.lookup(url);
            System.out.println("current balance = "+operationBancaire.balance());
                    operationBancaire.depot(200);
            System.out.println("updated balance = "+operationBancaire.balance());
                    operationBancaire.retrait(350);
            System.out.println("final balance = "+operationBancaire.balance());
        } catch (NotBoundException | MalformedURLException |
                 RemoteException ex) {
            ex.printStackTrace();
            System.out.print("Error while trying to access the server remotely");
        }
    }
}