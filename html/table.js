var tabledata = [{name: "Test", type: "int", get: true, value: 11}];
var table = new Tabulator("#example-table", {
    data: tabledata,           //load row data from array
    layout: "fitColumns",      //fit columns to width of table
    responsiveLayout: "hide",  //hide columns that dont fit on the table
    tooltips: true,            //show tool tips on cells
    addRowPos: "top",          //when adding a new row, add it to the top of the table
    history: true,             //allow undo and redo actions on the table
    pagination: "local",       //paginate the data
    paginationSize: 7,         //allow 7 rows per page of data
    movableColumns: true,      //allow column order to be changed
    resizableRows: true,       //allow row order to be changed
    initialSort: [             //set the initial sort order of the data
        { column: "name", dir: "asc" },
    ],
    dataChanged: function (data) {
        console.log(data)
        message.commands["table"] = data;
        SendMessage();
    },
    columns: [                 //define the table columns
        { title: "Name", field: "name", editor: "input" },
        { title: "Value", field: "value", editor: "input" }
    ],
});