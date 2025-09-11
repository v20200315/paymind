$(function () {
    $('#product_table').DataTable({
        processing: true,
        serverSide: true,
        ajax: BASE_URL + "api/sandbox/product/datatables/",
        columns: [
            {data: "id"},
            {data: "name"},
            {data: "description"},
            {data: "price"},
            {data: "stock"},
            {data: "status"},
            {data: "type"},
            {data: "created_at"},
            {data: "created_by"},
            {data: "updated_at"},
            {data: "updated_by"}
        ],
        pageLength: 10,
        order: []
    });
});