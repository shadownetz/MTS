class Purchase{

    constructor(productId){
        this.product_id = productId;
        this.amount = 0.0;
        this.quantity = 1;
        // this.sub_total = 0.0;
    }

    get sub_total(){
        return this.amount * (this.quantity===0||!this.quantity?1:this.quantity)
    }

}

class Sale{
    constructor(productId){
        this.product_id = productId;
        this.quantity = 1;
        this.discount = 0.0;
        this.amount = 0.0;
    }

    get get_total(){
        return (this.amount-((this.discount/100)*this.amount))*this.get_quantity
    }

    get get_quantity(){
        return (this.quantity===0||!this.quantity?1:this.quantity)
    }
}
class Product{
    constructor() {
        this.fetchProductsURL = $('#api_products_fetch_url');
    }

    static get_quantity(products=[], product_id){
        if(products){
            if(products.length > 0){
                let tmp_prod = products.filter(product=>product.id===product_id);
                if(tmp_prod.length > 0)
                    return tmp_prod[0].quantity
            }
        }
        return 0
    }

    async fetch_products(){
        let response = {status: true, products: []};
        try{
            response = await $.ajax({
                url: this.fetchProductsURL.val(),
                type: 'GET',
                // data: {},
                dataType: 'json',
            });
        }catch (e) {
            response.status = false;
            console.log('Error while fetching products:', e)
        }
        return Promise.resolve(response)
    }

}

function dispAlert(message='', type='info'){
    return Swal.fire({
        title: message,
        type,
        animation: !1,
        customClass: "animated flipInX",
        confirmButtonClass: "btn btn-primary",
        buttonsStyling: !1
    })
}