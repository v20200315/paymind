$(function () {
    $('#customer_table').DataTable({
        processing: true,
        serverSide: true,
        ajax: BASE_URL + "api/sandbox/customer/datatables/",
        columns: [
            {data: "id"},
            {data: "name"},
            {data: "email"},
            {data: "phone"},
            {data: "status"},
            {data: "created_at"},
            {data: "created_by"},
            {data: "updated_at"},
            {data: "updated_by"}
        ],
        pageLength: 10,
        order: []
    });
});