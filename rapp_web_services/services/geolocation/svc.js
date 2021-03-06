/***
 * Copyright 2015 RAPP
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * Authors: Konstantinos Panayiotou
 * Contact: klpanagi@gmail.com
 *
 */



/**
 * @fileOverview
 *
 * [Geolocation] RAPP Platform front-end web service.
 *
 *  @author Konstantinos Panayiotou
 *  @copyright Rapp Project EU 2015
 */


var path = require('path');

var interfaces = require( path.join(__dirname, 'iface_obj.js') );

const rosSrvName = "/rapp/rapp_geolocator/locate";


/**
 *  [Geolocation]
 *  Handles requests to geolocation RAPP Platform Service
 *
 *  Service Implementation.
 *
 */
function svcImpl(req, resp, ros) {
  if (! req.body.ipaddr) {
    // Retrieve client ip from request.
    // If the connection was established through a Proxy Server then the
    // returned information will be related to the Proxy Server location.
    req.body.ipaddr = req.socket.hostname;
  }

  var rosMsg = new interfaces.ros_req();
  rosMsg.ip = req.body.ipaddr;
  rosMsg.geolocator = req.body.engine;

  // ROS-Service response callback.
  function callback(data) {
    var response = parseRosbridgeMsg(data);
    resp.sendJson(response);
  }

  // ROS-Service onerror callback.
  function onerror(e) {
    var response = new interfaces.client_res();
    response.error = e;
    resp.sendJson(response);
  }

  // Call ROS-Service.
  ros.callService(rosSrvName, rosMsg, {success: callback, fail: onerror});
}




/***
 * Craft response object.
 *
 *  @param {Object} rosbridge_msg - Return message from rosbridge
 *  @returns {Object} response - Response Object.
 *  @returns {String} response.error - Error message.
 *  @returns {String} response.city
 *  @returns {String} response.country
 *  @returns {String} response.country_code
 *  @returns {String} response.latitude
 *  @returns {String} response.longtitude
 *  @returns {String} response.region
 *  @returns {String} response.timezone
 *  @returns {String} response.zip
 *
 */
function parseRosbridgeMsg(rosbridge_msg) {
  var response = new interfaces.client_res();

  const error = rosbridge_msg.error;

  if (error) {
    response.error = error;
    return response;
  }

  response.city = rosbridge_msg.city;
  response.country = rosbridge_msg.country;
  response.country_code = rosbridge_msg.countryCode;
  response.latitude = rosbridge_msg.latitude;
  response.longtitude = rosbridge_msg.longtitude;
  response.region = rosbridge_msg.regionName;
  response.timezone = rosbridge_msg.timezone;
  response.zip = rosbridge_msg.zip;

  return response;
}


module.exports = svcImpl;
