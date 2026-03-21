document.addEventListener('DOMContentLoaded', () => {
    const imageInput = document.getElementById('imageInput');
    const imagePreview = document.getElementById('imagePreview');
    const previewContainer = document.getElementById('previewContainer');
    const loader = document.getElementById('loader');
    const captionResult = document.getElementById('captionResult');

    imageInput.addEventListener('change', async (e) => {
        const file = e.target.files[0];
        if (!file) return;

        // Reset state
        captionResult.textContent = '';
        captionResult.style.display = 'none';
        
        // Show preview
        const reader = new FileReader();
        reader.onload = (e) => {
            imagePreview.src = e.target.result;
            previewContainer.style.display = 'block';
        };
        reader.readAsDataURL(file);

        // Prepare upload
        const formData = new FormData();
        formData.append('file', file);

        loader.style.display = 'block';

        try {
            const response = await fetch('/upload-image', {
                method: 'POST',
                body: formData
            });
            const data = await response.json();
            
            loader.style.display = 'none';
            if (data.error) {
                captionResult.textContent = `Error: ${data.error}`;
                captionResult.style.color = 'red';
            } else {
                captionResult.textContent = `"${data.caption}"`;
                captionResult.style.color = 'var(--text-color)';
            }
            captionResult.style.display = 'block';
        } catch (error) {
            loader.style.display = 'none';
            captionResult.textContent = 'An error occurred while generating the caption.';
            captionResult.style.color = 'red';
            captionResult.style.display = 'block';
            console.error('Error:', error);
        }
    });
});
