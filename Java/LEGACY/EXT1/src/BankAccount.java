//14010855
//¹Ú¼öÇÑ

public class BankAccount {
	private int accountNumber;
	private int balance;
	
	public BankAccount(int accountNumber) {
		this.accountNumber=accountNumber;
	}
	
	public BankAccount(int accountNumber, int balance) {
		this.accountNumber=accountNumber;
		this.balance=balance;
	}

	public int getAccountNumber() {
		return accountNumber;
	}
	
	public int getBalance() {
		return balance;
	}
	
	public boolean deposit(int amount) {
		if(amount>0) {
		this.balance+=amount;
		return true;
		}
		else
			return false;
	}
	
	public boolean withdraw(int amount) {
		if (this.balance-amount<0) {
			return false;
		}
		else {
			this.balance-=amount;
			return true;
		}
	}
	
	public boolean transfer(BankAccount other, int amount) {
		if (this.balance-amount<0)
			return false;
		else {
			this.balance-=amount;
			other.balance+=amount;
			return true;
		}
	}
	
	public String toString() {
		return "accountNumber : "+this.accountNumber+"	balance : "+this.balance;
	}
}
