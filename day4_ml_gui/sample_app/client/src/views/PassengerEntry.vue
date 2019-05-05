<template>
  <v-container
    fill-height
    fluid
    grid-list-xl>
    <v-layout
      justify-center
      wrap
    >
      <v-flex
        xs12
        md8
      >
        <material-card
          :color="color"
          title="Passenger Entry"
          text="Complete your entry form"
        >
          <v-form>
            <v-container py-0>
              <v-layout wrap>

                <v-flex
                  xs12
                  md6
                >
                  <v-text-field
                    v-model="firstName"
                    label="First Name"
                    class="purple-input"
                  />
                </v-flex>

                <v-flex
                  xs12
                  md6
                >
                  <v-text-field
                    v-model="lastName"
                    label="Last Name"
                    class="purple-input"
                  />
                </v-flex>

                <v-flex
                  xs12
                  md4
                >
                  <v-text-field
                    v-model="age"
                    label="Age"
                    class="purple-input"
                    type="number"
                  />
                </v-flex>

                <v-flex
                  xs12
                  md6
                >
                  <v-radio-group
                    v-model="sex"
                    label="Sex"
                    row
                  >
                    <v-radio
                      :value="0"
                      label="Female"
                    />
                    <v-radio
                      :value="1"
                      label="Male"
                    />
                  </v-radio-group>
                </v-flex>

                <v-flex
                  xs12
                  md4
                >
                  <v-text-field
                    v-model="familySize"
                    label="Family Size"
                    class="purple-input"
                    type="number"
                  />
                </v-flex>

                <v-flex
                  xs12
                  md4
                >
                  <v-text-field
                    v-model="embarkedOptions[embarked].name"
                    class="purple-input"
                    label="embarked"
                    @click="onOpenMapDialog"
                  />
                </v-flex>

                <v-flex
                  xs12
                  md12
                >
                  <v-slider
                    v-model="fare"
                    :hint="`You are eligible for CALSS ${pclass}`"
                    label="Budget for fare per person"
                    thumb-label="always"
                    min="0"
                    max="512"
                    persistent-hint
                    ticks
                  />
                </v-flex>

                <v-flex
                  xs12
                  text-xs-right
                >
                  <v-btn
                    class="mx-0 font-weight-light"
                    color="success"
                    @click="onSubmit()"
                  >
                    Register
                  </v-btn>
                </v-flex>

                <v-snackbar
                  :color="snackbar.color"
                  v-model="snackbar.visible"
                  top
                  right
                  dark
                >
                  <v-icon
                    color="white"
                    class="mr-3"
                  >
                    {{ snackbar.icon }}
                  </v-icon>
                  <div>{{ snackbar.text }}</div>
                  <v-icon
                    size="16"
                    @click="snackbar.visible = false"
                  >
                    mdi-close-circle
                  </v-icon>
                </v-snackbar>

              </v-layout>
            </v-container>
          </v-form>
        </material-card>
      </v-flex>

      <v-dialog
        v-model="mapDialog"
        fullscreen
        hide-overlay
        transition="dialog-bottom-transition"
      >
        <v-card>
          <v-card-title class="headline">Select port</v-card-title>

          <v-card-text>
            Select the port you embark
          </v-card-text>

          <v-radio-group
            v-model="embarked"
            row
          >
            <v-radio
              :value="0"
              label="Southampton"
            />
            <v-radio
              :value="1"
              label="Cherbourg"
            />
            <v-radio
              :value="2"
              label="Queenstown(Cobh)"
            />
          </v-radio-group>

          <div class="mapouter">
            <div class="gmap_canvas">
              <iframe
                id="gmap_canvas"
                :src="embarkedOptions[embarked].map"
                width="100%"
                height="100%"
                frameborder="0"
                scrolling="no"
                marginheight="0"
                marginwidth="0"
              />
            </div>
          </div>

          <v-card-actions>
            <v-spacer/>

            <v-flex
              xs12
              text-xs-right
            >
              <v-btn
                class="mx-0 font-weight-light"
                color="success"
                @click="onCloseMapDialog"
              >
                Location Confirmed
              </v-btn>
            </v-flex>

          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-layout>
  </v-container>
</template>

<script>
import {
  mapState
} from 'vuex'

export default {
  //
  data: () => ({
    mapDialog: false,
    snackbar: {
      visible: false,
      color: 'success',
      icon: 'success',
      text: ''
    },
    // snackbar: false,

    firstName: null,
    lastName: null,
    age: null,
    sex: null,
    fare: 0,
    familySize: null,
    embarked: 0,

    embarkedOptions: [
      {
        id: 0,
        name: 'Southampton',
        map: 'https://maps.google.com/maps?q=Southampton&t=&z=13&ie=UTF8&iwloc=&output=embed'
      },
      {
        id: 1,
        name: 'Cherbourg',
        map: 'https://maps.google.com/maps?q=Cherbourg-Octeville&t=&z=13&ie=UTF8&iwloc=&output=embed'
      },
      {
        id: 2,
        name: 'Queenstown(Cobh)',
        map: 'https://maps.google.com/maps?q=Cobh&t=&z=13&ie=UTF8&iwloc=&output=embed'
      }
    ]
  }),

  computed: {
    ...mapState('app', ['image', 'color']),
    pclass () {
      if (this.fare < 9) return 3
      if (this.fare < 16) return 2
      return 1
    }
  },
  methods: {
    onOpenMapDialog () {
      this.mapDialog = true
    },
    onCloseMapDialog () {
      this.mapDialog = false
    },
    onSubmit () {
      this.$axios.post('http://localhost:5000/api/passenger',
        {
          first_name: this.firstName,
          last_name: this.lastName,
          pclass: this.pclass,
          age: parseInt(this.age),
          sex: this.sex,
          fare: this.fare,
          family_size: parseInt(this.familySize),
          embarked: this.embarked
        }
      )
        .then(response => {
          this.snackbar = {
            visible: true,
            color: 'success',
            icon: 'mdi-check',
            text: 'Successfully registered'
          }
        })
        .catch(() => {
          this.snackbar = {
            visible: true,
            color: 'negative',
            icon: 'mdi-alert',
            text: 'Failed to register'
          }
        })
    }
  }
}
</script>

<style>
.mapouter {
  /* text-align:right; */
  height:100%;
  width:100%;
  /* position: absolute; */
}
.gmap_canvas {
  overflow:hidden;
  background:none!important;
  height:100%;
  width:100%;
}
</style>
