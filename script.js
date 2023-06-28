function searchResources() {
    var searchQuery = document.getElementById("search-input").value;
    var searchResults = performSearch(searchQuery);
    var resourceList = document.getElementById("resource-list");
    resourceList.innerHTML = "";

    if (searchResults.length == 0) {
        var noResults = document.createElement("li");
        noResults.textContent = "No results found";
        resourceList.appendChild(noResults);
    
    } else {
        for (var i = 0; i < searchResults.length; i++) {
            var resource = searchResults[i];
            var resourceItem = document.createElement("li");
            resourceItem.classList.add("resource-item");
            var title = document.createElement("h3");
            title.textContent = resource.name;
            var description = document.createElement("p");
            description.textContent = resource.description;
            resourceItem.appendChild(title);
            resourseItem.appendChild(description);
            resourceList.appendChild(resourceItem);
        }
    }
}

function performSearch(searchQuery) {
    var dummyData = [
        {
            name: "Resource 1",
            description: "This is a description of resource 1"
        },
        {
            name: "Resource 2",
            description: "This is a description of resource 2"
        },
        {
            name: "Resource 3",
            description: "This is a description of resource 3"
        }

    ];
    
    var filteredData = dummyData.filter(function(resource) {

        return resource.name.toLowerCase().includes(searchQuery.toLowerCase());
        
    });

    return filteredData;

}    