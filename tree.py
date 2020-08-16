
class node:
    def __init__(self):
        self.value = null
        self.left = null
        self.right = null

curr_val1 = "13"
curr_val2 = "12"
while(node.value is not null):
    if(node.left is not null):
        curr_val1 = curr_val1 + str(node.value)
        node = node.left
    else:
        curr_val1 = curr_val1 + str(node.value)
        node = node.right
    

while(node.right is not null):
    curr_val2 = curr_val2 + str(node.value)
    node = node.right

select("#monitoring donut")

    .on("click", d =>{
        d3.select("#dataviewsvg")
        .healthdatafilter(data)
    })

    healthdatafilter(data){
        return filtered data
    }

