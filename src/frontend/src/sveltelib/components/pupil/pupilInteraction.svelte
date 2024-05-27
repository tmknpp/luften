<script>
  import { selectedPupil, refreshMessagesTrigger } from "../../../stores/selectedPupil";
  import { createPupilMessage , reading_tutor, createPupilRun } from "../../../dataservices";
  import socketStore from "../../../stores/socket";

  let content1 = '';  
  let socket;

  socketStore.subscribe(value => {
    socket = value;
  });

  let userRole = (JSON.parse(localStorage.getItem('user')))?.role;

  async function performAction() {
    try {
      socket.emit("request_response", {
        'cmd': 'create_pupil_message',
        'respondAt': 'stream_tutor_response',
        'pupil_id': $selectedPupil[0],
        'assistant_id': $reading_tutor.assistant_id,
        'content': content1,
      });

      // Clear the textarea after submission
      content1 = '';
    } catch (error) {
      console.log(error);
    }
  }

  async function performAction2() {
    try {
      let result = await createPupilRun($selectedPupil[0], $reading_tutor.assistant_id);
      console.log(result);
    } catch (error) {
      console.log(error);
    }
  }
</script>

Pupil Interaction
<textarea bind:value={content1}></textarea>

<button on:click={performAction}> Submit</button>

{#if userRole == "admin"}
<button on:click={performAction2}> Create Run </button>
{/if}

<style>
  textarea {
    width: 100%;
    height: 200px;
  }
</style>
