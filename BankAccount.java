public class BankAccount {
    String name;
    String number;
    double balance;
    public BankAccount(String name, String number, double initialBalance) {
        this.name = name;
        this.number = number;
        this.balance = initialBalance;
    }
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("Deposit is successful and Balance is:"+balance);
        } else {
            System.out.println("Please enter a positive value.");
        }
    }
    public void withdraw(double amount) {
        if (amount > 0) {
            if (amount <= balance) {
                balance -= amount;
                System.out.println("Withdrawal is successful and Balance is:"+balance);
            } else {
                System.out.println("Insufficient funds. Withdrawal unsuccessful.");
            }
        } else {
            System.out.println("Please enter a positive value.");
        }
    }
    public void displayBalance() {
        System.out.println("-------------------------------");
        System.out.println("Account Holder: " + name);
        System.out.println("Account Number: " + number);
        System.out.println("Current Balance: $" + balance);
        System.out.println("-------------------------------");
    }

    public static void main(String[] args) {
        BankAccount myAccount = new BankAccount("Srinivas", "938188404789", 1000.0);
        myAccount.displayBalance();

        myAccount.deposit(500.0);
        myAccount.withdraw(200.0);
        myAccount.displayBalance();
    }
}
