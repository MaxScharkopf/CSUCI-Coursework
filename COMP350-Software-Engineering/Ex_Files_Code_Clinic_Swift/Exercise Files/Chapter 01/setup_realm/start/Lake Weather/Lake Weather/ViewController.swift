//
//  ViewController.swift
//  Lake Weather
//
//  Created by Todd Perkins on 4/16/18.
//  Copyright © 2018 Todd Perkins. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var activityView: UIView!
    @IBOutlet weak var medianSpeedLabel: UILabel!
    @IBOutlet weak var meanSpeedLabel: UILabel!
    @IBOutlet weak var meanPressureLabel: UILabel!
    @IBOutlet weak var medianPressureLabel: UILabel!
    @IBOutlet weak var meanTempLabel: UILabel!
    @IBOutlet weak var medianTempLabel: UILabel!
    @IBOutlet weak var startPicker: UIDatePicker!
    @IBOutlet weak var endPicker: UIDatePicker!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        activityView.isHidden = true
        loadRealm()
    }
    
    func loadRealm() {
        
    }
    
    @IBAction func didPressUpdate(_ sender: Any) {
        activityView.isHidden = false
        
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.01) {
            self.updateDays()
            self.activityView.isHidden = true
        }
        
    }
    
    func updateDays() {
        
    }
    
    func showMessage(message:String) {
        let alert = UIAlertController(title: "Missing Data", message: message, preferredStyle: .alert)
        let action = UIAlertAction(title: "Ok", style: .default, handler: nil)
        alert.addAction(action)
        self.present(alert, animated: true, completion: nil)
    }
    
    func findMean(a:[Double]) -> Double {
        return 0
    }
    
    func findMedian(a:[Double]) -> Double {
        return 0
    }
    
    @IBAction func startDateDidChange(_ sender: UIDatePicker) {
        // make sure end date is after start date
        if startPicker.date >= endPicker.date {
            //print("start date is after end date")
            endPicker.date = startPicker.date
        }
    }
    @IBAction func endDateDidChange(_ sender: UIDatePicker) {
        // make sure start date is before end date
        if startPicker.date >= endPicker.date {
            //print("start date is after end date")
            startPicker.date = endPicker.date
        }
    }
    
    override var prefersStatusBarHidden: Bool {
        return true
    }
    
    
}



