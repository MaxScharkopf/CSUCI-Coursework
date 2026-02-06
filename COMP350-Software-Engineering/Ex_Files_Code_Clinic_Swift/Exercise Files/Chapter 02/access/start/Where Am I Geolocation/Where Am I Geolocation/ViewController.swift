//
//  ViewController.swift
//  Where Am I Geolocation
//
//  Created by Todd Perkins on 3/16/18.
//  Copyright © 2018 Todd Perkins. All rights reserved.
//

import UIKit
import MapKit
import CoreLocation

// data from https://ipinfo.io/geo
struct IPData: Codable {
    var ip:String = ""
    var city:String = ""
    var region:String = ""
    var country:String = ""
    var loc:String = ""
}

class ViewController: UIViewController {
    @IBOutlet weak var ipLabel: UILabel!
    @IBOutlet weak var countryLabel: UILabel!
    @IBOutlet weak var stateLabel: UILabel!
    @IBOutlet weak var cityLabel: UILabel!
    @IBOutlet weak var map: MKMapView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        showIPData()
    }
    
    func showIPData() {
        
    }

}

