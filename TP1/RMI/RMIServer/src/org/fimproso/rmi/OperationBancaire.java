package org.fimproso.rmi;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface OperationBancaire extends Remote {

    double balance() throws RemoteException;
    void retrait(double amount) throws RemoteException;
    void depot(double amout) throws RemoteException;

}