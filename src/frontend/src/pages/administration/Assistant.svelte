<script>
    import { providers, models, reading_tutor } from "../../dataservices";
    import {createReadingTutor, refreshReadingTutor, updateReadingTutor} from "../../dataservices"
    import { marked } from "marked";

    let real_models = $models.reduce((acc, item) => ({ ...acc, ...item }), {});

    let selectedProvider = '';
   
    let availableModels = [];
    

    $: {

        if (selectedProvider !== undefined) {                        
            availableModels = real_models[selectedProvider] || [];
        }
    }


    
    async function createAssistant() {
        await createReadingTutor(selectedProvider, $reading_tutor.real_model, $reading_tutor.instructions)

    }

    async function updateAssistant() {
        await updateReadingTutor($reading_tutor.assistant_id,selectedProvider, $reading_tutor.real_model, $reading_tutor.instructions )
        await refreshReadingTutor()

    }

    async function deleteAssistant() {

    }


</script>

<div>
    <h2> Assistant Administration </h2>

</div>
<div>
Provider
{$reading_tutor.assistant_id}




<select bind:value={selectedProvider} >
    {#each $providers as provider}
        <option value={provider}>
            {provider}
        </option>
    {/each}
</select>

Model 


 
<select bind:value={$reading_tutor.real_model} >
    {#each availableModels as potential_model }
        <option value={potential_model}>
            {potential_model}
        </option>
    {/each}    
</select>



</div>


<div class="textareacontainer">
    <textarea bind:value={$reading_tutor.instructions}></textarea>
</div>

{#if $reading_tutor && $reading_tutor.assistant_id === null}

    <button on:click={createAssistant}>Create Assistant</button>

{:else}

    <button on:click={updateAssistant}>Update Assistant</button>
    <button on:click={deleteAssistant}>Delete Assistant</button>

{/if}


<style>

    .textareacontainer {
        display: flex;
        /* Adjust the container's attributes as needed */
        justify-content: space-between; 
        align-items: flex-start; 
    }
	    textarea {
           flex: 1; 
           margin: 10px; 
           min-width: 0; 
        }
    textarea {
        height: 300px; 
        resize: vertical; 
    }

</style>
