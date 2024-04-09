const productIdInput = document.getElementById('productId');
const imagesContainer = document.getElementById('imagesContainer');
const uploadForm = document.getElementById('uploadForm');
const fetchImagesButton = document.getElementById('fetchImages')

const imageInput = document.getElementById('imageInput');
const imagePreviews = document.getElementById('imagePreviews');

imageInput.addEventListener('change', () => {
    imagePreviews.innerHTML = '';  // Clear previous previews 

    for (let i = 0; i < imageInput.files.length; i++) {
        const file = imageInput.files[i];

        if (file) {
            const reader = new FileReader();
            const previewImg = document.createElement('img'); // Create a new <img> element

            reader.addEventListener('load', () => {
                previewImg.src = reader.result;
                imagePreviews.appendChild(previewImg); // Append to the container
            });

            reader.readAsDataURL(file);
        }
    }
});


// Fetch Images
fetchImagesButton.addEventListener('click', () => {
  const productId = productIdInput.value;
    fetchImages(productId);
});

function fetchImages(productId) {
    fetch(`http://127.0.0.1:7000/api/v1/products/${productId}/images/`)
    .then(response => response.json())
    .then(images => displayImages(images))
    .catch(error => console.error('Error fetching images:', error)); 
}

function displayImages(images) {
    imagesContainer.innerHTML = ''; // Reset content
    images.forEach(image => {
        const img = document.createElement('img');
        img.src = image.image; // Assuming 'image' field has the URL
        img.alt = image.descriptioin;

        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete'
        deleteButton.addEventListener('click', () => deleteImage(productId, image.id));

        const container = document.createElement('div');
        container.appendChild(img);
        container.appendChild(deleteButton);

        imagesContainer.appendChild(container);
    });
}

// Upload Image
uploadForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const productId = productIdInput.value;
    const formData = new FormData(uploadForm);
    uploadImage(productId, formData);
});

function uploadImage(productId, formData) {
    fetch(`http://127.0.0.1:7000/api/v1/products/${productId}/images/`, {
        method: 'POST',
        body: formData
    })
    .then(response => {
      if(response.ok){
         fetchImages(productId); // Refresh the image list
      } else {
         // Handle upload errors
      }
    })
    .catch(error => console.error('Error uploading image:', error));
}

// Delete Image (TODO: Implement) 
function deleteImage(productId, imageId) {
  // ...implementation for sending a DELETE request to `/api/products/${productId}/images/${imageId}/`
} 

