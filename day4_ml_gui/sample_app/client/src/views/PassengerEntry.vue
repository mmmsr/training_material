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
          color="cyan"
          title="Edit Profile"
          text="Complete your profile"
        >
          <v-form>
            <v-container py-0>
              <v-layout wrap>
                <!-- <v-flex
                  xs12
                  md4
                >
                  <v-text-field
                    label="Company (disabled)"
                    disabled/>
                </v-flex> -->
                <!-- <v-flex
                  xs12
                  md4
                >
                  <v-text-field
                    class="-purple-input"
                    label="User Name"
                  />
                </v-flex> -->
                <!-- <v-flex
                  xs12
                  md4
                >
                  <v-text-field
                    label="Email Address"
                    class="purple-input"/>
                </v-flex> -->
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
                  <v-text-field
                    label="Adress"
                    class="purple-input"/>
                </v-flex>
                <v-flex
                  xs12
                  md4>
                  <v-text-field
                    label="City"
                    class="purple-input"/>
                </v-flex>
                <v-flex
                  xs12
                  md4>
                  <v-text-field
                    label="Country"
                    class="purple-input"/>
                </v-flex>
                <v-flex
                  xs12
                  md4>
                  <v-text-field
                    class="purple-input"
                    label="Postal Code"
                    type="number"/>
                </v-flex>
                <v-flex xs12>
                  <v-textarea
                    class="purple-input"
                    label="About Me"
                    value="Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                  />
                </v-flex>
                <v-flex
                  xs12
                  text-xs-right
                >
                  <v-btn
                    class="mx-0 font-weight-light"
                    color="success"
                  >
                    Update Profile
                  </v-btn>
                </v-flex>
              </v-layout>
            </v-container>
          </v-form>
        </material-card>
      </v-flex>
      <!-- <v-flex
        xs12
        md4
        v-if="false"
      >
        <material-card class="v-card-profile">
          <v-avatar
            slot="offset"
            class="mx-auto d-block"
            size="130"
          >
            <img
              src="https://demos.creative-tim.com/vue-material-dashboard/img/marc.aba54d65.jpg"
            >
          </v-avatar>
          <v-card-text class="text-xs-center">
            <h6 class="category text-gray font-weight-thin mb-3">CEO / CO-FOUNDER</h6>
            <h4 class="card-title font-weight-light">Alec Thompson</h4>
            <p class="card-description font-weight-light">Don't be scared of the truth because we need to restart the human foundation in truth And I love you like Kanye loves Kanye I love Rick Owens’ bed design but the back is...</p>
            <v-btn
              color="success"
              round
              class="font-weight-light"
            >Follow</v-btn>
          </v-card-text>
        </material-card>
      </v-flex> -->
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
            <!-- src="https://maps.google.com/maps?q=google&t=&z=13&ie=UTF8&iwloc=&output=embed" -->
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
                @click="onCloseDialog"
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
export default {
  //
  data: () => ({
    mapDialog: false,
    firstName: null,
    lastName: null,
    pclass: null,
    age: null,
    sex: null,
    fare: null,
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
  methods: {
    onOpenMapDialog () {
      this.mapDialog = true
    },
    onCloseDialog () {
      this.mapDialog = false
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
