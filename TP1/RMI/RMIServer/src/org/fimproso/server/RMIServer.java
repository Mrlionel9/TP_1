package org.fimproso.server;

import org.fimproso.rmi.OperationBancaire;
import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;

public class RMIServer {
    public static void main(String[] args) {
        try {
            OperationBancaire bankObject = new BankServant();
            LocateRegistry.createRegistry(5099);
            String url = "rmi://localhost:5099/Bank";
            Naming.rebind(url, bankObject);
            System.out.println("Server RMI is ready and waiting...");

        } catch (RemoteException | MalformedURLException ex) {
            ex.printStackTrace();
            System.out.println("Error trying to connect to MathService object");
        }
    }
}