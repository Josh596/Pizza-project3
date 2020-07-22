document.addEventListener('DOMContentLoaded', () =>{
    
    
    
    //registering the modals and constant variables
    const modal = document.querySelector('.modals');
    let closeButton = document.querySelector('.close-button')


    //For displaying the modals
    function toggleModal() {
        modal.classList.toggle("show-modal");
        document.querySelector('.size_radio').innerHTML = ''
    }

   

    function windowOnClick(event) {
        if (event.target === modal) {
            toggleModal();
        }
    }

   

    document.querySelectorAll('.cards').forEach(card =>{
    
        card.addEventListener('click', () =>{
            item = card.dataset.item
            menu_name = card.dataset.menu
            console.log(item)
            //Load toggleModal
            toggleModal();
            //time to send the ajax requests
            let request = new XMLHttpRequest
            const request_data = JSON.stringify({"item_name":item, "menu_name":menu_name})
            request.open('GET', request_data)
            
            request.send()

            request.onload = () =>{
                let json_data = request.response
                console.log(json_data)
                //Getting data from the ajax request
                data = JSON.parse(json_data)
                console.log(data)
                let price = []
                let sizes = []
                for(info in data){
                    if('price' in data[info]['fields']){
                        item_price = data[info]['fields']['price']
                        //
                        price.push(item_price)                    
                                                        }
                    if('size' in data[info]['fields']){
                        item_size = data[info]['fields']['size']
                        if(item_size == 1){
                            sizes.push('Small')
                        }
                        else{
                            sizes.push('Large')
                        }
                        console.log('Work')
                    }                    
                                }
                    
                    for(size in sizes){
                        console.log(sizes[size])
                        console.log('It is present')
                        document.querySelector('.size_radio').innerHTML +=  `<label class="radio_container"><input type="radio" class = "size" name="radio" value = "${sizes[size]}">${sizes[size]}</label>`
                       
                        
                       

                    }                

                console.log(price)
               var small_price = Math.min.apply(null, price)
               var large_price = Math.max.apply(null, price)
                //Checking for small and large price
                if(small_price != large_price){
                    console.log(small_price)
                    console.log(large_price)
                   
                }
                else{
                    console.log(small_price)
                }

                           
                 //The content of the modal, toppings and co
            document.querySelector('.item3').innerHTML = `${small_price}+`
            document.querySelector('.order_button').innerHTML = `${small_price}`
            document.querySelectorAll('.radio_container').forEach(size =>{
                //Change total price on click radio
                size.onclick = () =>{
                    if(size.innerText == "Small"){
                    document.querySelector('.order_button').innerHTML = `${small_price}`
                    }
                    else{
                        document.querySelector('.order_button').innerHTML = `${large_price}`
                    }
                }
            })
//End of request.onload
            }
           
            //The quantity modal for the footer
            plus = document.querySelector('#plus')
            minus = document.querySelector('#minus')
            counter_input = document.querySelector('.counter_input')
            plus.onclick = () =>{
                counter_input.value ++
            }
             
            minus.onclick = () =>{
                if(counter_input.value >0){
                counter_input.value --
            }
            }
            counter_input.onkeyup = () =>{
               value = parseInt(counter_input.value, 10)
                    console.log(typeof value)
                   
                
                if(counter_input.value < 0){
                    counter_input.value = 0
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