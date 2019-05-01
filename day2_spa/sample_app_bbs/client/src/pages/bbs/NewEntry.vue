<template>
  <q-page
    class="docs-input row justify-center"
    padding
  >
    <div style="width: 500px; max-width: 90vw;">
      <h6 style="color: #027be3;">
        BBS Entry
      </h6>
      <q-input
        v-model="title"
        label="Title"
      />

      <q-input
        v-model="postedBy"
        label="Your Name"
      />

      <q-input
        v-model="body"
        type="textarea"
        label="Content"
      />
      <br>
      <q-btn
        color="primary"
        label="Submit"
        @click="submit()"
      />
    </div>
  </q-page>
</template>

<style></style>

<script>
export default {
  name: "NewEntry",
  data() {
    return {
      title: '',
      body: '',
      postedBy: ''
    }
  },
  methods: {
    submit() {
      this.$axios.post("http://localhost:5000/api/entry",
        {
          title: this.title,
          body: this.body,
          posted_by: this.postedBy
        }
      )
        .then(response => {
          this.$router.push('/bbs/entries')
          this.$q.notify({
            color: 'positive',
            position: 'top',
            message: 'Succesfully posted',
            icon: 'done'
          })
        })
        .catch(() => {
          this.$q.notify({
            color: 'negative',
            position: 'top',
            message: 'Loading failed',
            icon: 'report_problem'
          })
        })
    }
  }
}
</script>
