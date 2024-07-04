public class Venue {
    String venue_name;
    String address;
    public Venue(){};
    public Venue(String venue_name,String address){
        this.venue_name=venue_name;
        this.address=address;
    }
    public String getVenueName(){
        return venue_name;
    }
    public void setVenueName(String venue_name){
        this.venue_name=venue_name;
    }
    public String getAddress(){
        return address;
    }
    public void setAddress(String address){
        this.address=address;
    }
    public void display_venue_details(){
        System.out.println("Venue Name: "+this.getVenueName());
        System.out.println("Address: "+this.getAddress());
    }    
}