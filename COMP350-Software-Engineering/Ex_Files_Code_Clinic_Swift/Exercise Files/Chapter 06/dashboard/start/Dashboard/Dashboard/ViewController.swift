//
//  ViewController.swift
//  Dashboard
//
//  Created by Todd Perkins on 4/3/18.
//  Copyright © 2018 Todd Perkins. All rights reserved.
//

import UIKit
import Foundation
import RealmSwift

class DashboardData: Object {
    
    @objc dynamic var time_stamp: String? = nil
    let Pulsometer_readout = RealmOptional<Int>()
    let Engine_efficiency = RealmOptional<Double>()
    let red_Value = RealmOptional<Int>()
    let blue_Value = RealmOptional<Int>()
    let green_Value = RealmOptional<Int>()
}

class ViewController: UIViewController {
    var realm:Realm!
    var index:Int = 0
    var data:Results<DashboardData>!

    @IBOutlet weak var label: UILabel!
    @IBOutlet weak var label2: UILabel!
    @IBOutlet weak var colorView: UIView!
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        loadRealm()
    }
    
    func loadRealm() {
        do {
            // copy file to docs directory
            let fileManager = FileManager.default
            
            let documentsUrl = fileManager.urls(for: .documentDirectory,in: .userDomainMask)[0].appendingPathComponent("dashboard.realm")
            let bundledFile = Bundle.main.url(forResource: "dashboard", withExtension: "realm")!
            if !fileManager.fileExists(atPath: documentsUrl.path) {
                try fileManager.copyItem(at: bundledFile, to: documentsUrl)
            }
            
            var config = Realm.Configuration()
            config.objectTypes = [DashboardData.self]
            config.fileURL = documentsUrl
            realm = try Realm(configuration: config)
        } catch {
            print(error)
        }
    }
}

