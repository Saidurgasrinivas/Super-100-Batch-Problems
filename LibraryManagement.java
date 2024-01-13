import java.util.ArrayList;

import javax.security.auth.login.AppConfigurationEntry;

class Book{
    public int bookid;
    public String name;;
    public int year;
    public boolean isavl;
public Book(int bi,String n,int y)
{
    bookid=bi;
    name=n;
    year=y;
    this.isavl=true;
}
public  String display(){
    return "BookId:"+bookid+" Name:"+name+" Year:"+year+" Available:"+isavl;
}
}
class Library{
    String name;
    ArrayList<Book> books;
    public Library(String name)
    {
        this.name=name;
        books =new ArrayList<>();
    }
    void addbook(Book book)
    {
        books.add(book);
    }
    void displaybooks()
    {
        System.out.println("Books in Library");
        for(Book b: books)
        {
            System.out.println(b);
        }
    }
    void borrowing(Member m,int id)
    {
        for(Book b:books)
        {
            if(b.bookid==id && b.isavl)
            {
                b.isavl=false;
                m.getBorrowedBooks().add(b);
                System.out.print(m.name +" Borrowed book Successful");
                return;
            }
        }
    }
    void returning(Member m,int id)
    {
        for(Book b: m.getBorrowedBooks())
        {
            if(b.bookid==id)
            {
                b.isavl=true;
                m.getBorrowedBooks().remove(b);
                System.out.println(m.name+" Returned Book");
            }
            else
            System.out.print("Book Not Found");
        }
    }
}
class Member
{
    int id;
    String name;
    ArrayList<Book> borrowed;
    public Member(int id,String name)
    {
        this.id=id;
        this.name=name;
        this.borrowed=new ArrayList<>();
    }
    public ArrayList<Book> getBorrowedBooks(){
        return borrowed;
    }
    public void display()
    {
        System.out.println(name+" Borrowed Books");
        for(Book b: borrowed)
        {
            System.out.println(b);
        }
    }
}
public class Library {
    public static void main(String [] args)
    {
        Book b1=new Book(1,"DSA USING JAVA",1996);
        Book b2=new Book(2,"DSA USING PYTHON",1987);
        Book b3=new Book(3,"DSA USING C",1967);
        Library l=new Library("College Library");
        l.addbook(b1);
        l.addbook(b2);
        l.addbook(b3);
        Member m1=new Member(11, "Srinivas");
        Member m2=new Member(12,"Vasu");
        l.displaybooks();
        l.borrowing(m1, 1);
        l.displaybooks();
        l.returning(m1, 1);
    }
}
