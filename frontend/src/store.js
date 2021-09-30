export default {
    state: {
        contact: false
    },
    ContactForm(){
        this.state.contact = true
        console.log(this.state.contact)
    },
    killContactForm(){
        this.state.contact = false
    }
}