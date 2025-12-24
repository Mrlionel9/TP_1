package org.fimproso.server;
import org.fimproso.rmi.OperationBancaire;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class BankServant extends UnicastRemoteObject implements
        OperationBancaire {
    private double amount = 3000;
    public BankServant() throws RemoteException{
        super();
    }

    @Override
    public double balance() throws RemoteException {
        return amount;
    }
    @Override
    public void retrait(double amount) throws RemoteException {
        this.amount -=amount;
    }

    @Override
    public void depot(double amount) throws RemoteException {
        this.amount +=amount;
    }

}