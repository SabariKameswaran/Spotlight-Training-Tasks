import java.sql.Date;
import java.sql.Time;

class Event{
    private String event_name;
    private Date event_date;
    private Time event_time;
    private String venue_name;
    private int total_seats;
    private int available_seats;
    private double ticket_price;
    enum event_type{Movie,Sports,Concert};
    Event(){};
    Event(String event_name, Date event_date, Time event_time, String venue_name, int total_seats, int available_seats, double ticket_price, event_type event_type){
        this.event_name = event_name;
        this.event_date = event_date;
        this.event_time = event_time;
        this.venue_name = venue_name;
        this.total_seats = total_seats;
        this.available_seats = available_seats;
        this.ticket_price = ticket_price;
    }
    public String getName(){
        return event_name;
    }
    public void setName(String event_name){
        this.event_name = event_name;
    }
    public Date getDate(){
        return event_date;
    }
    public void setDate(Time event_time){
        this.event_time = event_time;
    }
    public Time getTime(){
        return event_time;
    }
    public void setTime(Time event_time){
        this.event_time = event_time;
    }
    public String getVenueName(){
        return venue_name;
    }
    public void setVenueName(String venue_name){
        this.venue_name = venue_name;
    }
    public int getTotalSeats(){
        return total_seats;
    }
    public void setTotalSeats(int total_seats){
        this.total_seats = total_seats;
    }
    public int getAvailableSeats(){
        return available_seats;
    }
    public void setAvailableSeats(int available_seats){
        this.available_seats = available_seats;
    }
    public double getTicketPrice(){
        return ticket_price;
    }
    public void setTicketPrice(double ticket_price){
        this.ticket_price = ticket_price;
    }
    public double Calculate_total_revenue(){
        double total_revenue = total_seats * ticket_price;
        return total_revenue;
    }
    public int getBookedNoOfTickets(){
        int booked_ticket = total_seats - available_seats;
        return booked_ticket;
    }
    public void book_tickets(int num_tickets){
        if(num_tickets <= available_seats)
            available_seats -= num_tickets;
    }
    public void cancel_tickets(int num_tickets){
        available_seats+=num_tickets;
    }
    public void display_event_details(){
        System.out.println("Event Name: " + this.getName());
        System.out.println("Event Date: " + this.getDate());
        System.out.println("Event Time: " + this.getTime());
        System.out.println("Venue Name: " + this.getVenueName());
        System.out.println("Total Seats: " + this.getTotalSeats());
        System.out.println("Available Seats: " + this.getAvailableSeats());
        System.out.println("Ticket Price: " + this.getTicketPrice());
        System.out.println("Total Revenue: " + Calculate_total_revenue());
        System.out.println("Booked Tickets: " + getBookedNoOfTickets());
    }
    
}