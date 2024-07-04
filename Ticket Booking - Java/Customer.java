public class Customer {
    String customer_name;
    String email;
    int phone_number;

    Customer(){};
    public Customer(String custom_name,String email,int phone_number){
        this.customer_name = custom_name;
        this.email = email;
        this.phone_number = phone_number;
    }
    public String getCustomerName(){
        return customer_name;
    }
    public void setCustomerName(String custom_name){
        this.customer_name = custom_name;
    }
    public String getEmail(){
        return email;
    }
    public void setEmail(String email){
        this.email = email;
    }
    public int getPhoneNumber(){
        return phone_number;
    }
    public void setPhoneNumber(int phone_number){
        this.phone_number = phone_number;
    }
    public void display_customer_details(){
        System.out.println("Customer Name: " + customer_name);
        System.out.println("Email: " + email);
        System.out.println("Phone Number: " + phone_number);
    }
}