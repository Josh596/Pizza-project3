document.addEventListener('DOMContentLoaded', () =>{
    
    
    
    //registering the modals and constant variables
    const modal = document.querySelector('.modals');
    let closeButton = document.querySelector('.close-button')


    //For displaying the modals
    function toggleModal() {
        modal.classList.toggle("show-modal");
    }

   

    function windowOnClick(event) {
        if (event.target === modal) {
            toggleModal();
        }
    }

    document.querySelectorAll('.cards').forEach(card =>{
    
        card.addEventListener('click', () =>{
            item = card.dataset.item
            console.log(item)
            //Load toggleModal
            toggleModal();
            //time to send the ajax requests
            let request = new XMLHttpRequest
            request.open('GET', `/${item}`)
            
            request.send()

            request.onload = () =>{
                let json_data = request.response
                //Getting data from the ajax request
                data = JSON.parse(json_data)
                console.log(data)
                let price = []
                for(info in data){
                    if('price' in data[info]['fields']){
                        item_price = data[info]['fields']['price']
                        //
                        price.push(item_price)                    
                                                        }                    
                                }

                console.log(price)
                small_price = Math.min.apply(null, price)
                large_price = Math.max.apply(null, price)
                //Checking for small and large price
                if(small_price != large_price){
                    console.log(small_price)
                    console.log(large_price)
                }
                else{
                    console.log(small_price)
                }


            }
            
        })
    })

    //Sample output
   // [{"model": "orders.items", "pk": 1, "fields": {"menu": 1, "name": "Regular Cheese Pizza"}}, 
    //{"model": "orders.item_price", "pk": 1, "fields": {"item": 1, "price": "12.70", "size": 1}}, 
   // {"model": "orders.item_price", "pk": 2, "fields": {"item": 1, "price": "17.95", "size": 2}}]

    closeButton.addEventListener("click", toggleModal)
    document.addEventListener("click", windowOnClick);

























})